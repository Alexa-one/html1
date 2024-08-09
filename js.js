let num = 50;
if (num < 49) {
  console.log("Неправильно!");
} else if (num > 100) {
  console.log("Багато");
} else {
  console.log("Правильно!");
}

num == 50 ? console.log("Правильно!") : console.log("Неправильно!");

switch (num) {
  case num < 49:
    console.log("Неправильно!");
    break;
  case num > 100:
    console.log("Багато!");
    break;
  case num > 80:
    console.log("Досі багато!");
    break;
  case num == 50:
    console.log("Правильно!");
    break;
  default:
    console.log("Щось пішло не так!");
    break;
}

// while (num < 55) {
//   console.log(num);
//   num++;
// }

do {
  console.log(num);
  num++;
} while (num < 55);

for (let i = 1; i < 8; i++) {
  if (i == 6) {
    continue;
  }
  console.log(i);
}
