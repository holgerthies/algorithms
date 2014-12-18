
// Graph is given is adjacency matrix (vector<vector<int>>)

int bfs(const vector<vector<int>>& G, const int s, const int t, vector<int>& parent){
	int n = G.size();
	vector<bool> visited(n, false);
	queue<int> q;
	q.push(s);
	visited[s] = true;
	int min_cut=INF;
	while(!q.empty()){
		int v = q.front();
		q.pop();
		for(int i=0; i<n;i++){
			if(!visited[i] && G[v][i] > 0){
				visited[i] = true;
				parent[i] = v;
				q.push(i);
				min_cut = min(min_cut, G[v][i]);
				if(i == t)
					return min_cut;
			}
		}
	}
	return 0;
}

int maxflow(vector<vector<int>> G, const int s, const int t){
	bool increment=true;
	int n = G.size();
	int ans=0;
	while(increment){
		vector<int> parent(n, -1);
		int flow=bfs(G, s, t, parent);
		if(flow > 0){
			int curr=t;
			ans+=flow;
			while(curr != s){
				G[parent[curr]][curr] -= flow;
				G[curr][parent[curr]] += flow;
				curr = parent[curr];
			}
		} else{
			increment=false;
		}
	}
	return ans;
}

