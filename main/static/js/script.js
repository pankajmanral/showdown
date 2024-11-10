// sidebar navigation

const toggleBtn = document.querySelector('#toggleBtn')
const sidebar = document.querySelector('#sidebar')

toggleBtn.addEventListener('click',()=>{
    sidebar.classList.toggle("-translate-x-full")
    sidebar.classList.toggle("translate-x-0")
})

// cart dropdown 

const cartDropdown = document.querySelector("#cartDropdown")
const addCartBtn = document.querySelectorAll("#addCartBtn")
const crossBtn = document.querySelectorAll("#crossBtn")

addCartBtn.forEach((button) =>{
    button.addEventListener("click",()=>{

        const productName = button.getAttribute('data-product-name')
        const productImage = button.getAttribute('data-product-img')
        
        document.querySelector("#dropdownName").textContent = productName
        document.querySelector("#dropdownImage").src = productImage
        
        cartDropdown.classList.remove("-translate-y-full","opacity-0")

        setTimeout(()=>{
            closeFunction()
        },5000)
    
    })
})

const closeFunction = () => {
    cartDropdown.classList.add("-translate-y-full")
}

crossBtn.forEach((btn) => {
    btn.addEventListener("click",closeFunction)
})

// user menu

const usermenu = document.querySelector("#usermenu");
const user = document.querySelector("#user");

user.addEventListener("click", () => {
    
    if(usermenu.classList.contains("opacity-0")){
        usermenu.classList.remove("opacity-0")
    }
    else{
        usermenu.classList.add("opacity-0")
    }

});

document.addEventListener("click", (event) => {
    if (!usermenu.contains(event.target) && event.target !== user) {
        usermenu.classList.add("opacity-0");
    }
});


// summary dropdown for smaller devices 
// add the script file here 