import {Feline} from './Feline'

export class Cat extends Feline{
    static nCats : number = 0;
    meow : string;
    name : string;

    constructor(habitat: string, family: string, meow: string, name: string) {
        super(habitat, family);
        this.meow = meow;
        this.name = name;
        Cat.nCats++;
    }

    talk() {
        return this.meow;
    }
}