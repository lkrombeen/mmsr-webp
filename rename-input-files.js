const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('input');

for (const file of files) {
  if (
    file.indexOf('(') === -1
    && file.indexOf('_') === -1
    && file.indexOf(' ') === -1
    && file.toLowerCase() === file) {
    continue;
  }
  const content = fs.readFileSync(path.join('input', file));
  fs.writeFileSync(path.join('input', file.replace(/\(|\)|_| /g, '').toLowerCase()), content);
  fs.unlinkSync(path.join('input', file));
}
