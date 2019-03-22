let N = 5;
let M = 6;

// Create random matrix
let matrix = new Array(N);
for (let i = 0; i < N; ++i) {
    matrix[i] = new Array(M);
    for (let j = 0; j < M; ++j) {
        matrix[i][j] = Math.floor(Math.random() * 10);
    }
}
console.log("Original");
console.log(matrix);

// Gather zeros
let zeros = [];
for (let i = 0; i < matrix.length; ++i) {
    for (let j = 0; j < matrix[0].length; ++j) {
        if (matrix[i][j] == 0) {
            zeros.push({
                i: i,
                j: j
            });
        }
    }
}

// Populate rows and columns with zeros
zeros.forEach(zero => {
    for (let i = 0; i < matrix.length; ++i) {
        matrix[i][zero.j] = 0;
    }
    for (let j = 0; j < matrix[0].length; ++j) {
        matrix[zero.i][j] = 0;
    }
});

console.log("Zeroed");
console.log(matrix);
