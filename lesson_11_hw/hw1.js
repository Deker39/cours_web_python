// Uncomment the code to see the work
/*          Exercise 1              */
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
// kek.square_circle()
// kek.length_circle()

/*----------------------------------*/
/*          Exercise 2              */

class HtmlElement{

    #tag_name
    #self_closing
    #text_content
    #array_attributes
    #array_style
    #array_nested_tag
    static main_string = new String
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
        console.log(`tag_name: ${this.#tag_name},\nself_closing: ${this.#self_closing},\
        \ntext_content: ${this.#text_content},\narray_attributes: ${this.#array_attributes},\
        \narray_style: ${this.#array_style},\narray_nested_tag: ${this.#array_nested_tag}`);
    }
    attribute_setting(){  
        let att = []
        
        if (this.#array_attributes !== null){
            for (var i = 0;i<this.#array_attributes.length;i++){
                att[i] = `${this.#array_attributes[i][0]}="${this.#array_attributes[i][1]}"`
            }
            att = att.join('')
        }
        else att = ""

        return att
    }

    style_setting(){
        let sty = []
        let sty_res

        if (this.#array_style !== null){
            for (var i = 0;i<this.#array_style.length;i++){
                sty[i] = `${this.#array_style[i][0]}:${this.#array_style[i][1]};`
                sty_res = `style="${sty}"`
            }
        }
        else sty_res = ""

        return sty_res
    }

    add_nested_element_to_start(){
        let nes_tag = []

        if (this.#array_nested_tag !== null){
            for (var i = 0;i<this.#array_nested_tag.length;i++){
                nes_tag[i]= `${this.#array_nested_tag[i]}`  
            }
            nes_tag = nes_tag.join('')
           
        }
        else nes_tag = ""
        
        return nes_tag
    }

    add_nested_element_to_end(){
        let nes_tag = []
        if (this.#array_nested_tag !== null){
            for (var i = 0;i<this.#array_nested_tag.length;i++){
                nes_tag[i]= `${this.#array_nested_tag[i]}`  
            }
            nes_tag = nes_tag.join('')
        
        }
        else nes_tag = ""

        return nes_tag 
    }
    getHtml(){
        let main_string
        let end_tag
        let tc

        if (this.#self_closing == true){
            end_tag = `</${this.#tag_name}>`
        }
        else   end_tag = ""

        if (this.#text_content !== null){
            tc = `${this.#text_content}`
             
         }
         else tc = ""
        
        return main_string = `<${this.#tag_name} ${this.attribute_setting()} ${this.style_setting()}>\
        ${tc} ${this.add_nested_element_to_end()} ${end_tag}`
    }

    }

let text = ' Lorem, ipsum dolor sit amet consectetur adipisicing elit. Mollitia quis assumenda totam doloribus aut maxime \
            repellendus minus numquam porro, natus ex delectus accusantium error sapiente corporis asperiores, a adipisci suscipit.'

const a = new HtmlElement('a',true,'More...',[['href','https://ru.lipsum.com/'],['target','_blank']],null,null)
const p = new HtmlElement('p',true,text,[['class','text']],[['text-align','justify']],[a.getHtml()])
const img  = new HtmlElement('img',false,null,[['class','img'],['alt','lorem ipsum'],['src','lipsum.jpg']],[['width','100%']],null)
const h3 = new HtmlElement('h3',true,'What is Lorem Ipsum?',null,null,null) 
const div2 = new HtmlElement('div',true,null,[['class','block']],[['width','50%'],['margin','10px']],[h3.getHtml(),img.getHtml(),p.getHtml()])
const div1 = new HtmlElement('div',true,null,[['id','wrapper'],['class','wrap']],[['display','flex']],[div2.getHtml()])

// // div1.show()
// console.log(div1.getHtml());
// document.write(div1.getHtml())

/*----------------------------------*/
/*          Exercise 3              */

class CssClass extends HtmlElement{

    #name_class
    #stayle_array
    constructor(name_class,stayle_array,tag_name,self_closing,text_content,array_attributes,
        array_style,array_nested_tag){
        super(tag_name,self_closing,text_content,array_attributes,
            array_style,array_nested_tag)
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
        console.log(`name_class: ${this.#name_class},\narray_style: ${this.#stayle_array}`);
    }

    style_setting(){
        var name_sty = new String
        if (this.#stayle_array !== null){
            for (var i = 0;i<this.#stayle_array.length;i++){
                name_sty = name_sty + `${this.#stayle_array[i][0]}:${this.#stayle_array[i][1]}; `
            }
        }
        else name_sty = ""

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
        let sty
        this.#name_class !== null ? sty = `.${this.#name_class}`: sty = ""
        let sty_arr = this.style_setting()
        sty_arr !== null ? sty += `{${sty_arr}}` : sty=""
        console.log(sty);
        return sty
    }
}

let css = new CssClass('wrap',[['display','flex']])
let css1 = new CssClass('block',[['width','300px'],['margin','10px']])
let css2 = new CssClass('img',[['width','100%']])
let css3 = new CssClass('text',[['text-algin','justify']])

// css.show()
// css.getCss()
// css1.getCss()
// css2.getCss()
// css3.getCss()
// css1.style_remove()


/*----------------------------------*/
/*          Exercise 4              */


class HtmlBlock extends CssClass{

    #obj_css
    #obj_html
    constructor(obj_css,obj_html){
        super()
        this.obj_css = obj_css
        this.obj_html = obj_html
    }

    set obj_css(obj_css){
        this.#obj_css = obj_css
    }
    get obj_css(){
        return this.#obj_css
    }
    set obj_html(obj_html){
        this.#obj_html = obj_html
    }
    get obj_html(){
        return this.#obj_html
    }

    getCode(){
        let style 
        let sty =[]
        
        for(var i =0;i<this.#obj_css.length;i++){
            sty[i] = this.#obj_css[i].getCss()
        }      
        if(document.getElementsByTagName('style').length == 0 || document.getElementsByTagName('style') !== true) { 
            style = document.createElement('style');
            style.append(` ${sty.join('')}`)
        }
        else{ 
            style = document.body.querySelector('style')
            style.append(` ${sty.join('')}`)   
        }
        document.body.prepend(style)
        document.write(this.#obj_html.getHtml())
        
    }
 
}
const obj = new HtmlBlock([css,css1,css2,css3],div1)
obj.getCode()







