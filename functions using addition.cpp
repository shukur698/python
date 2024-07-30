#include<stdio.h>
int print(int n){
	for(i=1;i<=n;i++){
		printf("%d",i)
	}
}
int main(){
	int a;
	printf("enter the number");
	scanf("%d",&a);
	return print(a);
}