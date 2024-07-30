#include<stdio.h>
int main(){
	int rows1=3,cols1=3;
	int rows2=3,cols2=3;
	int matrix1[3][3]={{1,2,3},{4,5,6}};
	int matrix2[3][3]={{4,5,7},{6,7,9},{8,9,5}};
	int result[3][3]={0};
for(int i=0;i<rows1;i++){
	for(int j=0;j<cols2;j++){
		for(int k=0;k<cols1;k++){
			result[i][j]=matrix1[i][k]*matrix2[k][j];
		}
	}
}
printf("resultant matrix");
for(int i=0;i<rows1;i++){
	for(int j=0;j<cols2;j++){
		printf("  %d  ",result[i][j]);
	}
	printf("\n");
}
return 0;
	}