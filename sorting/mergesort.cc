#include <iostream>
template <typename T>
void merge(T* items, int low, int middle, int high){
	T* copy = new T[high-low+1];
	int pos_l = low;
	int pos_r = middle+1;
	int count = 0;
	while(count <= high-low){
		if(pos_r > high || (pos_l<=middle &&items[pos_l] <= items[pos_r])){
			copy[count++] = items[pos_l];
			pos_l++;
		}
		else {
			copy[count++] = items[pos_r];
			pos_r++;
		}
	}
	for(int i=low;i<=high;i++){
		items[i] = copy[i-low];
	}
	delete copy;
}

template <typename T>
void mergeSort(T* items, int low, int high){
	if(low < high){
		int middle = (low+high)/2;
		mergeSort(items, low, middle);
		mergeSort(items, middle+1, high);
		merge(items, low, middle, high);
	}
}