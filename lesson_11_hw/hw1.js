class Circle{

    #radius
    constructor(radius){
        this.#radius = radius
    }
    square_circle(){
        var square = Math.PI * this.radius**2
        console.log(`Radius: ${Math.floor(square)}`);
    }
    length_circle(){
        var length = Math.PI * this.diametr
        console.log(`Lenght: ${Math.floor(length)}`);
    }
    get radius(){
        return this.#radius
    }
    set radius(radius){
        this.#radius = radius
    }
    get diametr(){
        return this.#radius*2
    }

}

let kek  = new Circle(4)
kek.square_circle()
kek.length_circle()

class HtmlElement{

    static main_string = new String
    #tag_name
    #self_closing
    #text_content
    #array_attributes
    #array_style
    #array_nested_tag
    constructor(tag_name,self_closing,text_content,array_attributes,
                array_style,array_nested_tag){
                this.#tag_name = tag_name   || null
                this.#self_closing = self_closing  || null
                this.#text_content = text_content || null
                this.#array_attributes = array_attributes || null
                this.#array_style = array_style  || null
                this.#array_nested_tag = array_nested_tag  || null
            }

    set tag_name(tag_name){
        this.#tag_name = tag_name
    }

    get tag_name(){
        return this.#tag_name
    }

    set self_closing(self_closing){
        this.#self_closing = self_closing
    }

    get self_closing(){
        return this.#self_closing
    }

    set text_content(text_content){
        this.#text_content = text_content
    }

    get text_content(){
        return this.#text_content
    }

    set array_attributes(array_attributes){
        this.#array_attributes = array_attributes
    }

    get array_attributes(){
        return this.#array_attributes
    }

    set array_style(array_style){
        this.#array_style = array_style
    }

    get array_style(){
        return this.#array_style
    }

    set array_nested_tag(array_nested_tag){
        this.#array_nested_tag = array_nested_tag
    }

    get array_nested_tag(){
        return this.#array_nested_tag
    }

    show(){
        console.log(`tag_name: ${this.#tag_name},
self_closing: ${this.#self_closing}, 
text_content: ${this.#text_content},
array_attributes: ${this.#array_attributes},
array_style: ${this.#array_style},
array_nested_tag: ${this.#array_nested_tag}`);
    }

    attribute_setting(tag){  
        if (this.#array_attributes !== null){
            for (var i = 0;i<this.#array_attributes.length;i++){
                tag.setAttribute(this.#array_attributes[i][0], this.#array_attributes[i][1])
            }
        }
        else{}
       
    }

    style_setting(tag){
        if (this.#array_style !== null){
            for (var i = 0;i<this.#array_style.length;i++){
                tag.style[this.#array_style[i][0]] = this.#array_style[i][1] 
            }
        }
        else{}
    }
    getHtml(){
        const elem = document.createElement(this.#tag_name)
        this.attribute_setting(elem)
        this.style_setting(elem)
        document.body.prepend(elem)
        elem.innerHTML = this.#text_content
        this.add_nested_element_to_end()
        console.log(elem);
    }

    add_nested_element_to_end(){
        if (this.#array_nested_tag !== null){
            
            let ml = this.#array_nested_tag
            console.log(ml[`this.#array_style`]);
            // this.attribute_setting(this.#array_nested_tag)
        }
      
    }
    add_nested_element_to_start(){
        // let name = this.#tag_name
        // if(this.#array_nested_tag !== null){
        //     document.name.append(this.#array_nested_tag[0])
        // }
        // else{}
    }

   

    }

let text = ' Lorem, ipsum dolor sit amet consectetur adipisicing elit. Mollitia quis assumenda totam doloribus aut maxime \
            repellendus minus numquam porro, natus ex delectus accusantium error sapiente corporis asperiores, a adipisci suscipit.'


let p = new HtmlElement('p',true,text,null,[['text-align','justify']],null)
let img  = new HtmlElement('img',false,null,[['alt','lorem ipsum'],['src','lipsum.jpg']],[['width','100%']],null)
let h3 = new HtmlElement('h3',true,'What is Lorem Ipsum?',null,null,null)
let div2 = new HtmlElement('div',true,null,null,[['width','300px'],['margin','10px']],[h3,img,p])
let div1 = new HtmlElement('div',true,null,[['id','wrapper']],[['display','flex']],[div2])

// div1.show()
div1.getHtml()

class CssClass{

    #name_class
    #stayle_array
    constructor(name_class,stayle_array){
        this.#name_class = name_class || null
        this.#stayle_array = stayle_array || null 
    }

    set name_class(name_class){
        this.#name_class = name_class
    }
    get name_class(){
        return this.#name_class
    }

    set stayle_array(stayle_array){
        this.#stayle_array = stayle_array
    }

    get stayle_array(){
        return this.#stayle_array
    }
    show(){
        console.log(`name_class: ${this.#name_class},
array_style: ${this.#stayle_array}`);
    }

    style_setting(name_sty){
        var name_sty = new String
        if (this.#stayle_array !== null){
           
            for (var i = 0;i<this.#stayle_array.length;i++){
                name_sty = name_sty + `${this.#stayle_array[i][0]}:${this.#stayle_array[i][1]};`
            }
        }
        else{}

        return name_sty
    }
    style_remove(){
        let rem, rem1 = new String
        rem =  document.body.children[0].innerHTML
        rem1 = rem
        let first = rem.indexOf(`.${this.#name_class}`)
        let second = rem.indexOf(`}`,rem.indexOf(`${this.#name_class}`))
        rem = rem.substring (first,second+1)
        rem = rem1.replace(rem,'')
        let style = document.body.querySelector('style')
        style.replaceChildren(rem,'')

    }

    getCss(){
        let sty = `.${this.#name_class}`
        let sty_arr = this.style_setting(sty)
        // this.style_remove()
        sty += `{${sty_arr}}` 
        console.log(sty);
        let style
        if(document.getElementsByTagName('style').length == 0) {  

            style = document.createElement('style');
            style.append(` ${sty}`)
            console.log(style);
        
        }
        else{ 
            style = document.body.querySelector('style')
            style.append(` ${sty}`)
            
        }
        document.body.prepend(style)

    }
}

let css = new CssClass('wrap',[['display','flex'],['margin','10px']])
let css1 = new CssClass('kke',[['display','flex'],['margin','20px']])
// css.show()
// css.getCss()
// css1.getCss()
// css1.style_remove()


