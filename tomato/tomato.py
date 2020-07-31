# created by: https://github.com/itsKaspar
#modified by: https://github.com/LukasDrsman

import os, re, random, struct, sys
from itertools import chain
from itertools import repeat

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def bstream_until_marker(bfilein, bfileout, marker=0, startpos=0):
	chunk = 1024
	filesize = os.path.getsize(bfilein)
	if marker :
		marker = str.encode(marker)

	with open(bfilein,'rb') as rd:
		with open(bfileout,'ab') as wr:
			for pos in range(startpos, filesize, chunk):
				rd.seek(pos)
				buffer = rd.read(chunk)

				if marker:
					if buffer.find(marker) > 0 :
						marker_pos = re.search(marker, buffer).start()
						marker_pos = marker_pos + pos
						split = buffer.split(marker, 1)
						wr.write(split[0])
						print(marker_pos)
						return marker_pos
					else:
						wr.write(buffer)
				else:
					wr.write(buffer)

def glitchify(filein, mode, audio=0, firstframe=1, countframes=1, positframes=1, kill=0.7):
    temp_nb = random.randint(10000, 99999)
    temp_dir = "temp-" + str(temp_nb)
    temp_hdrl = temp_dir +"/hdrl.bin"
    temp_movi = temp_dir +"/movi.bin"
    temp_idx1 = temp_dir +"/idx1.bin"

    os.mkdir(temp_dir)

	movi_marker_pos = bstream_until_marker(filein, temp_hdrl, "movi")
	idx1_marker_pos = bstream_until_marker(filein, temp_movi, "idx1", movi_marker_pos)
	bstream_until_marker(filein, temp_idx1, 0, idx1_marker_pos)

	with open(temp_movi,'rb') as rd:
		chunk = 1024
		filesize = os.path.getsize(temp_movi)
		frame_table = []

		for pos in range(0, filesize, chunk):
			rd.seek(pos)
			buffer = rd.read(chunk)

			for m in (re.finditer(b'\x30\x31\x77\x62', buffer)):
					if audio : frame_table.append([m.start() + pos, 'sound'])
			for m in (re.finditer(b'\x30\x30\x64\x63', buffer)):
				frame_table.append([m.start() + pos, 'video'])

			frame_table.sort(key=lambda tup: tup[0])

		l = []
		l.append([0,0, 'void'])
		max_frame_size = 0

		for n in range(len(frame_table)):
			if n + 1 < len(frame_table):
				frame_size = frame_table[n + 1][0] - frame_table[n][0]
			else:
				frame_size = filesize - frame_table[n][0]
			max_frame_size = max(max_frame_size, frame_size)
			l.append([frame_table[n][0],frame_size, frame_table[n][1]])
		clean = []
		final = []

		if firstframe :
			for x in l :
				if x[2] == 'video':
			 		clean.append(x)
			 		break

		for x in l:
			if x[1] <= (max_frame_size * kill) :
				clean.append(x)

		if mode == "void":
			final = clean

		elif mode == "random":
			final = random.sample(clean,len(clean))

		elif mode == "reverse":
			final = clean[::-1]

		elif mode == "invert":
			final = sum(zip(clean[1::2], clean[::2]), ())

		elif mode == 'bloom':
			repeat = int(countframes)
			frame = int(positframes)
			lista = clean[:frame]
			listb = clean[frame:]
			final = lista + ([clean[frame]]*repeat) + listb

		elif mode == 'pulse':
			pulselen = int(countframes)
			pulseryt = int(positframes)
			j = 0
			for x in clean:
				i = 0
				if(j % pulselen == 0):
					while i < pulselen :
						final.append(x)
						i = i + 1
				else:
					final.append(x)
					j = j + 1

		elif mode == "jiggle":
			amount = int(positframes)
			final = [clean[constrain(x+int(random.gauss(0,amount)),0,len(clean)-1)] for x in range(0,len(clean))]

		elif mode == "overlap":
			pulselen = int(countframes)
			pulseryt = int(positframes)

			clean = [clean[i:i+pulselen] for i in range(0,len(clean),pulseryt)]
			final = [item for sublist in clean for item in sublist]

		else:
			final = clean

		cname = '-c' + str(countframes) if int(countframes) > 1 else ''
		pname = '-n' + str(positframes) if int(positframes) > 1 else ''
		fileout = filein[:-4] + '-' + mode + cname + pname + '.avi'

		if os.path.exists(fileout):
			os.remove(fileout)

		bstream_until_marker(temp_hdrl, fileout)

		with open(temp_movi,'rb') as rd:
			filesize = os.path.getsize(temp_movi)
			with open(fileout,'ab') as wr:
				wr.write(struct.pack('<4s', b'movi'))
				for x in final:
					if x[0] != 0 and x[1] != 0:
						rd.seek(x[0])
						wr.write(rd.read(x[1]))

		bstream_until_marker(temp_idx1, fileout)

        os.remove(temp_hdrl)
        os.remove(temp_movi)
        os.remove(temp_idx1)
        os.rmdir(temp_dir)

		if sys.platform == "linux":
			os.system('xdg-open ' + fileout)
		elif sys.paltform == "darwin":
			os.system('open ' + fileout)
		else:
			os.system('start ' + fileout)
