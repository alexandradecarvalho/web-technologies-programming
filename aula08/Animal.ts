export class Animal{
    static nAnimals: number = 0;
    habitat: string;

    constructor(habitat : string) {
        this.habitat = habitat;
        Animal.nAnimals++;
    }

    show(){
        return `${Animal.nAnimals} animals live in in ${this.habitat}`;
    }
}