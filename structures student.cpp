#include<stdio.h>
#include<string.h>

struct employee
{
	char name[100];
	int num;
	int salary;
	
};
int main(){
	struct employee*ptr,e;
	ptr=&e;
	printf("enter the name of student");
	scanf("%s",&ptr->name);
	printf("num");
	
	scanf("%d",&ptr->num);
	printf("salary of employee");
	scanf("%d",&ptr->salary);
	printf("name of student=%s",&ptr->name);
	printf("name of employee=%s",&ptr->name);
	printf("\n");
	printf("salary employee=%d",ptr->salary);

	}