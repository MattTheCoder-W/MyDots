#include <stdio.h>

int main(int argc, char** argv){
	char ch;
	FILE *fp;

	fp = fopen(argv[1], "r");

	if (fp == NULL){
		printf("Error reading file!");
		return 1;
	}

	while((ch = fgetc(fp)) != EOF){
		printf("%c", ch);
	}
	return 0;
}
