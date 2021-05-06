import {Animal} from './Animal'

export class Mammal extends Animal{
    static nMammals: number = 0;

    constructor(habitat: string) {
        super(habitat);
        Mammal.nMammals++;
    }

    talk() {
        return "..."
    }

    show(){
        return `${Mammal.nMammals} mammals do ${this.talk()}`;
    }


}