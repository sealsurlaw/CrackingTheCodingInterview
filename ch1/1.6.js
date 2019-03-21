let str = "aaaabbbbbbbbcccccccaaaaa"

console.log(str);

let compressStr = (str) => {
	if (str == null || str.length == 0) return str;

	let tempStr = '';
	let counter = 1;
	let currChar = str.charAt(0);

	for (let i = 1; i < str.length; ++i) {
		if (str.charAt(i) == currChar) {
			counter++;
		}
		else {
			tempStr += currChar + counter;
			currChar = str.charAt(i);
			counter = 1;
		}
	}
	tempStr += currChar + counter;
	if(tempStr.length <= str.length) return tempStr;
	return str;
}

console.log(compressStr(str));
