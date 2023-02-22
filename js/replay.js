while (true) {
  const s = prompt('Enter something: ');
  if (s == 'quit') {
    break;
  }
  console.log(`Length of the string is ${s.length}`);
}
console.log('Done');
