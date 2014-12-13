
vector<int> primes(const int N){
	vector<bool> is_prime(N+1, true);
	for(int p=2; p<=sqrt(N); p++){
		if(is_prime[p]){
			int j=p*p;
			while(j <= N){
				is_prime[j] = false;
				j += p;
			}
		}
	}
	vector<int> ans;
	ans.push_back(2);
	for(int p=3; p<=N; p+=2){
		if(is_prime[p]){
			ans.push_back(p);
		}
	}
	return ans;
}

vector<pair<int,int>> factor(const int N, const vector<int>& prime_list, const int start=0){
	if(N <= 1)
		return vector<pair<int,int>>();
	for(int i=start; i<prime_list.size() && prime_list[i] <= sqrt(N); i++){
		int p=prime_list[i];
		if(N % p == 0){
			int c=0;
			int M=N;
			while(M % p == 0){
				M /= p;
				c++;
			}
			auto ans = factor(M, prime_list, i+1);
			ans.push_back(make_pair(p,c));
			return ans;
		}
	}
	return vector<pair<int,int>>{make_pair(N,1)};
}
