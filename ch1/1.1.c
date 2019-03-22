#include <stdio.h>
#include <stdbool.h>

char* str1 = "Does this have unique characters?";
char* str2 = "abcdefghijklmnop";

bool hasUnique(char* str) {

	int uniqueArray[128];
	// Populate array with zeros
	for (int i = 0; i < 128; ++i) {
		uniqueArray[i] = 0;
	}

	for (int i = 0; str[i] != '\0'; ++i) {
		if (uniqueArray[str[i]] == 1)
			return false;
		else
			uniqueArray[str[i]]++;
	}
	return true;
}

void main() {
	printf("%s: %d\n", str1, hasUnique(str1));
	printf("%s: %d\n", str2, hasUnique(str2));
}
