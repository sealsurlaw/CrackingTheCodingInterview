#include <stdio.h>

void urlify(char* str, int length);

void main() {
	char str1[21] = "This is a test";
	int len1 = 21;

	printf("%s\n", str1);
	urlify(str1, len1);
	printf("%s\n", str1);
}

void urlify(char* str, int length) {
	for (int i = 0; i < length; ++i) {
		if (str[i] == ' ') {
			// Shift characters over by 2 after space
			for (int j = length-3; j > i; --j) {
				str[j+2] = str[j];
			}
			// Insert %20 in place of space
			str[i]   = '%';
			str[i+1] = '2';
			str[i+2] = '0';
		}
	}
}
