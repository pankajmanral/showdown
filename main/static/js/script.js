const toggleBtn = document.querySelector('#toggleBtn')
const sidebar = document.querySelector('#sidebar')

toggleBtn.addEventListener('click',()=>{
    sidebar.classList.toggle("-translate-x-full")
    sidebar.classList.toggle("translate-x-0")
})

const cartDropdown = document.querySelector("#cartDropdown")
const addCartBtn = document.querySelectorAll("#addCartBtn")
const crossBtn = document.querySelectorAll("#crossBtn")

addCartBtn.forEach((button) =>{
    button.addEventListener("click",()=>{

        cartDropdown.classList.remove("-translate-y-full")

        const productImage = this.getAtt

    })
})

const openFunctioin = () => {
    cartDropdown.classList.remove("-translate-y-full")

    setTimeout(()=>{
        closeFunction()
    },5000)

}

const closeFunction = () => {
    cartDropdown.classList.add("-translate-y-full")
}

addCartBtn.forEach((btn) =>{
    btn.addEventListener("click",openFunctioin)
})

crossBtn.forEach((btn) => {
    btn.addEventListener("click",closeFunction)
})