let price = 288.2789;
console.log(price.toFixed(1));
console.log("price :" + price.toString());
console.log(price.toPrecision(2));
console.log(price.toExponential());
console.log(price.toLocaleString("en-US", {
        style: "currency",
        currency: "USD",
    })
);
console.log("MAX_VALUE:", Number.MAX_VALUE);
console.log("MIN_VALUE:", Number.MIN_VALUE);
console.log("MAX_SAFE_INTEGER:", Number.MAX_SAFE_INTEGER);
console.log("MIN_SAFE_INTEGER:", Number.MIN_SAFE_INTEGER);
console.log("POSITIVE_INFINITY:", Number.POSITIVE_INFINITY);
console.log("NEGATIVE_INFINITY:", Number.NEGATIVE_INFINITY);
console.log("EPSILON:", Number.EPSILON);
console.log("NaN:", Number.NaN);