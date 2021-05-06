import {Animal} from "./Animal";
import {Mammal} from "./Mammal";
import {Reptile} from "./Reptile"
import {Canine} from "./Canine";
import {Feline} from "./Feline";
import {Cat} from "./Cat";
import {Dog} from "./Dog";

console.log("WELCOME")
let animal = new Animal("Earth")
console.log(animal.show())

console.log("\n-------------------------")
let reptile = new Reptile("Water")
let mammal = new Mammal("Earth")
console.log(mammal.show())

console.log("\n-------------------------")
let canine = new Canine("garden", "golden retriever")
let dog = new Dog("garden", "golden retriever", "woof woof")
console.log(dog.talk())

console.log("\n-------------------------")
let feline = new Feline("garden", "persa idk")
let cat = new Cat("garden", "golden retriever", "meow meow", "Fisga")
console.log(cat.talk())