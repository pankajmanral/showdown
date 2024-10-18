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

        const productName = button.getAttribute('data-product-name')
        const productImage = button.getAttribute('data-product-img')
        
        document.querySelector("#dropdownName").textContent = productName
        document.querySelector("#dropdownImage").src = productImage
        
        cartDropdown.classList.remove("-translate-y-full")

        setTimeout(()=>{
            closeFunction()
        },2000)
    
    })
})

const closeFunction = () => {
    cartDropdown.classList.add("-translate-y-full")
}

crossBtn.forEach((btn) => {
    btn.addEventListener("click",closeFunction)
})

// const openFunctioin = () => {
//     cartDropdown.classList.remove("-translate-y-full")
// }


// addCartBtn.forEach((btn) =>{
//     btn.addEventListener("click",openFunctioin)
// })
