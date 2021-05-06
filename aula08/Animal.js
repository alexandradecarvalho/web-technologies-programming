"use strict";
exports.__esModule = true;
exports.Animal = void 0;
var Animal = /** @class */ (function () {
    function Animal(habitat) {
        this.habitat = habitat;
        Animal.nAnimals++;
    }
    Animal.prototype.show = function () {
        return Animal.nAnimals + " animals live in in " + this.habitat;
    };
    Animal.nAnimals = 0;
    return Animal;
}());
exports.Animal = Animal;
