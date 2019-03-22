let s1 = 'dog';
let s2 = 'god';

let s3 = 'helloworld';
let s4 = 'fizzbuzz';

function isPermutation(str1, str2) {
	if (str1.length != str2.length) return false;


	let sum = 0;
	for (let i = 0; i < str1.length; i++) {
		sum += str1.charCodeAt(i);
		sum -= str2.charCodeAt(i);
	}
	if (sum == 0) return true;

	return false;
}

console.log(s1 + ', ' + s2 + ': ' + isPermutation(s1,s2));
console.log(s3 + ', ' + s4 + ': ' + isPermutation(s3,s4));
