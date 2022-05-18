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
                this.#tag_name = tag_name  || null
                this.#self_closing = self_closing || null
                this.#text_content = text_content || null
                this.#array_attributes = array_attributes || null
                this.#array_style = array_style  || null
                this.#array_nested_tag = array_nested_tag  || null
            }

    show(){
        console.log(`tag_name: ${this.#tag_name},
self_closing: ${this.#self_closing},
text_content: ${this.#text_content},
array_attributes${this.#array_attributes},
array_style: ${this.#array_style},
array_nested_tag: ${this.#array_nested_tag},
        `);
    }
    attribute_setting(){
        if(this.#self_closing == true){
            if( this.#text_content !== null){
                if( this.#array_nested_tag !== null){
                    var main_string =`<${this.#tag_name} ${this.#array_attributes} ${this.#array_style}>\
                    ${this.#text_content} ${this.#array_nested_tag} </${this.#tag_name}>`
                }
                else{
                    var main_string =`<${this.#tag_name} ${this.#array_attributes} ${this.#array_style}>\
                    ${this.#text_content}</${this.#tag_name}>`
                }
               
            }else{
                var main_string =`<${this.#tag_name} ${this.#array_attributes} ${this.#array_style}>\
               ${this.#array_nested_tag} </${this.#tag_name}>`
            }
            
        }else{
            main_string =`<${this.#tag_name}>`
        }
        return main_string
       
    }

    style_setting(){
        this.attribute_setting()
  
    }
    add_nested_element_to_end(){}
    add_nested_element_to_start(){}


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

    getHtml(){
        document.write(this. attribute_setting())
        console.log(this. attribute_setting());
    }


    }
let h3 = new HtmlElement('h2',true,'What is Lorem Ipsum?',null,null,null)
let div2 = new HtmlElement('div',true,null,null,'style=\'wigth:300px; margin:10px\'',h3.attribute_setting())
let div1 = new HtmlElement('div',true,null,'id=\'wrapper\'','style=\'display:flex;\'',div2.attribute_setting())
div2.show()
div1.show()
div1.getHtml()