#!/usr/bin/node
if (process.argv[2] === undefined) {
    process.argv[2] = undefined;
} else if (process.argv[3] === undefined) {
    process.argv[3] = undefined;
}
console.log(process.argv[2], 'is' , process.argv[3])
