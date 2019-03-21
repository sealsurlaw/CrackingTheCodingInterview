let N = 5;

let matrix = new Array(N);

for (let i = 0; i < N; ++i) {
	matrix[i] = new Array(N);
	for (let j = 0; j < N; ++j) {
		matrix[i][j] = Math.floor(Math.random() * 100);
	}
}

console.log(matrix);


let rotateMatrix = (mat, dir) => {

	// Mirror along y-axis
	if (dir == 'cw') {
		for (let i = 0; i < mat.length; ++i) {
			for (let j = 0; j < Math.floor(mat.length / 2); ++j) {
				let temp = mat[i][j];
				mat[i][j] = mat[i][mat.length - j - 1];
				mat[i][mat.length - j - 1] = temp;
			}
		}
	}
	else {
		for (let i = 0; i < Math.floor(mat.length / 2); ++i) {
			for (let j = 0; j < mat.length; ++j) {
				let temp = mat[i][j];
				mat[i][j] = mat[mat.length - i - 1][j];
				mat[mat.length - i - 1][j] = temp;
			}
		}
	}

	// Mirror diagonally
	let stop = mat.length - 1;
	for (let i = 0; i < mat.length - 1; ++i, --stop) {
		for (let j = 0; j < stop; ++j) {
			let temp = mat[i][j];
			mat[i][j] = mat[mat.length - 1 - j][mat.length - 1 - i];
			mat[mat.length - 1 - j][mat.length - 1 - i] = temp;
		}
	}

	return mat;
}

console.log("Counter Clockwise:");
console.log(rotateMatrix(matrix, 'ccw'));

console.log("Clockwise:");
console.log(rotateMatrix(matrix, 'cw'));

