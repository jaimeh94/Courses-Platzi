const lista1 = [
  1,
  2,
  3,
  1,
  2,
  3,
  4,
  2,
  2,
  2,
  1,
];

const lista1Count = {};

lista1.map(
  function (elemento) {
    if (lista1Count[elemento]) {
      lista1Count[elemento] += 1;
    } else {
      lista1Count[elemento] = 1;
    }
  }
);

const lista1Array = Object.entries(lista1Count).sort(
  function (elementoA, elementoB) {
    return elementoA[1] - elementoB[1];
  }
);

const moda = lista1Array[lista1Array.length - 1];

/*
function calcularModa(valores) {
  const [repeticiones, moda] = valores.reduce(
    (acc, val) => {
      const nn = contar(valores, val);
      if (nn === acc[0] && acc[1].every((item) => item !== val)) {
        acc[1].push(val);
      } else if (nn > acc[0]) {
        acc = [nn, [val]];
      }
      return acc;
    },
    [0, []]
  );

  return { repeticiones, moda };
}

function contar(arrayElmentos, valorAContar) {
  return arrayElmentos.filter((elemento) => elemento === valorAContar).length;
}
*/
