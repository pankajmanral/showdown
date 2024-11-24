// sidebar navigation

const toggleBtn = document.querySelector('#toggleBtn')
const sidebar = document.querySelector('#sidebar')

toggleBtn.addEventListener('click',()=>{
    sidebar.classList.toggle("-translate-x-full")
    sidebar.classList.toggle("translate-x-0")
})

// cart dropdown 

const cartDropdown = document.querySelector("#cartDropdown")
const crossBtn = document.querySelectorAll("#crossBtn")

const addCartBtn = document.querySelectorAll("#addCartBtn")
addCartBtn.forEach((button) =>{
    button.addEventListener("click",function(e){
        e.preventDefault()
        const productName = button.getAttribute('data-product-name')
        const productImage = button.getAttribute('data-product-img')
        const prodId = this.dataset.productId

        const csrfToken = document.cookie.split(';')
            .find(cookie => cookie.trim().startsWith('csrftoken='))
            ?.split('=')[1];

        document.querySelector("#dropdownName").textContent = productName
        document.querySelector("#dropdownImage").src = productImage

        fetch(`/cart/add-to-cart/${prodId}/`,{
            method : "POST",
            headers : {
                'Content-Type' : 'application/json',
                'X-CSRFToken': csrfToken, 
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            
        })
        
        cartDropdown.classList.remove("-translate-y-full","opacity-0")

        setTimeout(()=>{
            closeFunction()
        },3000)
    
    })
})

const closeFunction = () => {
    cartDropdown.classList.add("-translate-y-full","opacity-0")
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

// product_details

