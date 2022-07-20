class PrintMaсhine{
    constructor(fontSize,color,fontFamily){
        this.fontSize = fontSize;
        this.color = color;
        this.fontFamily = fontFamily;

    }

    print(text){
        var output = document.write(`<div class='border m-4 p-2'><p style="color:${this.color};font-size:${this.fontSize};
                                    font-family:${this.fontFamily}">${text}</p></div>`)

    }

}

let font = new PrintMaсhine(24,'red','sans-serif')

font.print('Lorem ipsum')


class Paragraf{
    constructor(title,publicationDate,text,arrayTags){
        this.title = title;
        this.text = text;
        this.arrayTags = arrayTags;
        this.publicationDate = publicationDate;
    }

    print(){
     
        var dataWrite = this.publicationDate.split('.').reverse()

        var diff = Math.abs(new Date() - new Date(dataWrite));
        
        var milliseconds = diff;
        var days = milliseconds / 1000 / 60 / 60 / 24

        var div = document.createElement('div')
        var h1 = document.createElement('h1')
        h1.textContent = this.title
        var date = document.createElement('p')
        date.classList.add('fw-bold')
        if (Math.ceil(days) == 1){
            date.textContent = 'Today'
        }
        else if(Math.ceil(days) < 8 && days > 1){
            date.textContent = `${Math.ceil(days)} days ago`
        }
        else date.textContent = this.publicationDate

        var p = document.createElement('p')
        p.textContent = this.text
        var tag = document.createElement('p')
        tag.textContent = this.arrayTags
        document.body.append(div)
        div.classList.add('border','m-4','p-2')
        div.appendChild(h1)
        div.appendChild(date)
        div.appendChild(p)
        div.appendChild(tag)

    }
}

let par1 = new Paragraf('Waht is Lorem Ipsum?','20.07.2022','Lorem ipsum dolor sit amet consectetur, adipisicing \
                    elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
                    Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#lorem \
                    #ipsum #text')
let par2 = new Paragraf('Waht is Lorem Ipsum?','16.07.2022','Lorem ipsum dolor sit amet consectetur, adipisicing \
                    elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
                    Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#lorem \
                    #ipsum #text')
let par3 = new Paragraf('Waht is Lorem Ipsum?','20.07.2000','Lorem ipsum dolor sit amet consectetur, adipisicing \
                    elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
                    Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#lorem \
                    #ipsum #text')

par1.print()
par2.print()
par3.print()