let str1 = 'waterbottle';
let str2 = 'erbottlewat';

function isRotation(s1, s2) {

    if (s1.length != s2.length) return false;

    for (let i = 0; i < s1.length; ++i) {
        if (s1 == s2) return true;

        // Rotate s2 by 1 to the left
        let temp = '';
        for (let j = 1; j < s2.length; ++j) {
            temp += s2.charAt(j);
        }
        s2 = temp + s2.charAt(0);
    }

    return false;
}

console.log(isRotation(str1, str2));