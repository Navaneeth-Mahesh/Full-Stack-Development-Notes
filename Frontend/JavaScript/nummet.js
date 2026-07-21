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
