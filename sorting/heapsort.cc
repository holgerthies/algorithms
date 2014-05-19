#include <utility>
#include <iostream>
using namespace std;

template<typename T>
void print(T* a, int len);

template <typename T>
void siftDown(T* a, int i, int end){
	int max=i;
	int left_child = 2*i+1;
	int right_child = 2*i+2;
	if(left_child <= end && a[left_child] > a[max])
		max = left_child;
	if(right_child <= end && a[right_child] > a[max])
		max = right_child;
	if(max != i){
		swap(a[i], a[max]);
		siftDown(a, max, end);
	}
}
template <typename T>
void heapify(T* a, int start, int end){
	int parent = (end-start)/2;
	for(int i=parent; i>=0; i--){
		siftDown(a, i, end); 
	}
}
template <typename T>
void heapsort(T* a, int start, int end){
	heapify(a, start, end);
	while(end > start){
		swap(a[0], a[end]);
		end--;
		siftDown(a, 0, end);
	}
}
template <typename T>
void print(T* a, int len){
	for(int i=0; i<len;i++){
		cout << a[i] << ",";
	}
	cout << endl;
}
int main(){
	float a1[] = {0.5,0.7,0.004,0.1,34.3};
	int a2[] = {23, 1,4,89,9,84,4};
	heapsort(a1, 0,4);
	heapsort(a2, 0,6);
	print(a1, 5);
	print(a2, 7);
	return 0;
}