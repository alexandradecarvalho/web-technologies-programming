import {Canine} from './Canine'

export class Dog extends Canine{
    static nDogs : number = 0;
    bark : string;

    constructor(habitat: string, race: string, bark: string) {
        super(habitat, race);
        this.bark = bark;
        Dog.nDogs++;
    }

    talk() {
        return this.bark;
    }
}