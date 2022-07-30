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


class NewsFeed extends Paragraf{
  
    constructor(arrayNews = []){
        super()
        this.arrayNews = arrayNews;
    }

    get getamountNews(){
        return this.arrayNews.length;
    }
    
    printAll(){
        
        var tit = document.createElement('h1')
        tit.textContent = 'News feed'
        tit.classList.add('d-flex', 'justify-content-center')
        document.body.appendChild(tit)

        for(var i = 0; i < this.getamountNews; i++){
            this.title = this.arrayNews[i].title;
            this.text = this.arrayNews[i].text;
            this.arrayTags = this.arrayNews[i].arrayTags;
            this.publicationDate = this.arrayNews[i].publicationDate
            this.print()
        }
    }

    addNews(obj){
        this.arrayNews.push(obj)
        console.log(`add new news: ${obj}`);
    
    }

    removeNews(obj){
        if (typeof(obj) == 'object'){
            this.arrayNews.splice(this.arrayNews.indexOf(obj),1)
        }else if(typeof(obj) == 'number'){
            this.arrayNews.splice(obj,1)
        }
        else{ alert('type error')}
    }
    sortNews(){
        var date = []
        var dateShort =[]
        var newArray = []
        for(var i = 0;i < this.getamountNews; i++){
            date[i] = new Date(this.arrayNews[i].publicationDate.split('.').reverse())
        }
        const sortedActivities = date.slice().sort((a, b) => b - a)
        for (var i =0;i< sortedActivities.length;i++){
            dateShort[i]=sortedActivities[i].toLocaleDateString()
        }

        for(var i = 0;i < dateShort.length; i++){
            for (var j =0;j< this.getamountNews;j++){
                if(dateShort[i]== this.arrayNews[j].publicationDate){
                    newArray[i]=this.arrayNews[j]
                }
            }
        }

        for(var i = 0;i < this.getamountNews; i++){
            this.arrayNews[i] = newArray[i]
        }    
     
    }
    searchTag(tag){
        var tags = []
        var find = []
        for(var i = 0;i < this.getamountNews; i++){
            tags[i] = this.arrayNews[i].arrayTags  
            
        }    

        for(var i =0;i<tags.length;i++){
            if (tags[i].indexOf(tag) > 0){
                find.push(i)
            }
        }
      
       for(var i =0;i< find.length;i++){
        console.log(this.arrayNews[find[i]])
       }
        
        
    }

}

function News(title,publicationDate,text,arrayTags) {
    this.title = title;
    this.text = text;
    this.arrayTags = arrayTags;
    this.publicationDate = publicationDate;
  }

  
let newsOdject1 = new News('1 News','20.07.2002','Lorem ipsum dolor sit amet consectetur, adipisicing \
elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#lorem #ipsum #text')

let newsOdject2 = new News('2 News','16.07.2021','Lorem ipsum dolor sit amet consectetur, adipisicing \
elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#soluta #porro #modi')

let newsOdject3 = new News('3 News','20.07.2017','Lorem ipsum dolor sit amet consectetur, adipisicing \
elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#molestiae #reprehenderit #iusto')

let news1 = new NewsFeed([newsOdject1,newsOdject2,newsOdject3]) 

news1.addNews(new News('4 News','20.07.2022','Lorem ipsum dolor sit amet consectetur, adipisicing \
elit. Eos earum saepe molestiae sit ab reprehenderit asperiores iusto totam cum. \
Consequuntur, sint? Est, porro soluta modi ducimus maiores odio ad eum!','#molestiae #totam #cum'))

// news1.removeNews(1) // write object or index
news1.sortNews()
news1.printAll()
news1.searchTag('molestiae')
