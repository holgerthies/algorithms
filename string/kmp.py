def _build_table(P):
	m = len(P)
	F = [0]*(m+1)
	for i in range(1,m+1):
		k = i-1
		while k>0 and P[F[k]] != P[i-1]:
			k = F[k]
		if k == 0:
			F[i] = 0
		else:
			F[i] = F[k]+1
	return F

def search(S, P):
	word_pos = 0
	pattern_pos = 0
	m = len(P)
	n = len(S)
	F = _build_table(P)
	c=0
	while word_pos+pattern_pos < n:
		if S[word_pos+pattern_pos] == P[pattern_pos]:
			pattern_pos += 1
			if pattern_pos == m:
				yield word_pos
				word_pos += pattern_pos
				pattern_pos = 0
		else:
			word_pos += pattern_pos-F[pattern_pos]+1
			pattern_pos = F[pattern_pos]
	return 




