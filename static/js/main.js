(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Initiate the wowjs
  new WOW().init();

  // Sticky Navbar
  $(window).scroll(function () {
    if ($(this).scrollTop() > 45) {
      $(".navbar").addClass("sticky-top shadow-sm");
    } else {
      $(".navbar").removeClass("sticky-top shadow-sm");
    }
  });

  // Dropdown on mouse hover
  const $dropdown = $(".dropdown");
  const $dropdownToggle = $(".dropdown-toggle");
  const $dropdownMenu = $(".dropdown-menu");
  const showClass = "show";

  $(window).on("load resize", function () {
    if (this.matchMedia("(min-width: 992px)").matches) {
      $dropdown.hover(
        function () {
          const $this = $(this);
          $this.addClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "true");
          $this.find($dropdownMenu).addClass(showClass);
        },
        function () {
          const $this = $(this);
          $this.removeClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "false");
          $this.find($dropdownMenu).removeClass(showClass);
        }
      );
    } else {
      $dropdown.off("mouseenter mouseleave");
    }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    center: true,
    margin: 24,
    dots: true,
    loop: true,
    nav: false,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
    },
  });
})(jQuery);

// ADD product to cart
// var product_id = document.getElementById("add-button");
// var csrfToken = "{{csrf_token}}";
// var action = "post";
// const url = '{% url "cart:add_to_cart" %}'
// console.log(url)

// product_id.addEventListener("click", function(e) {
//     e.preventDefault()
//     if (e.target.id === "add-button") {
//       fetch(url, {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/x-www-form-urlencoded",
//         },
//         body: new URLSearchParams({
//           productid: product_id.value,
//           csrfmiddlewaretoken: csrfToken,
//           action: action,
//         }),
//       })
//         .then(function(response) {
//           if (response.ok) {
//             // Handle the success response here
//             return response.text();
//           }
//           throw new Error("Request failed.");
//         })
//         .then(function(data) {
//           // Handle the success data here
//           // ...
//         })
//         .catch(function(error) {
//           // Handle errors here
//           console.log(error);
//         });
//     }
//   });

// $('.add-to-cart').on("click", "#add-button", function (e) {
//   e.preventDefault();
//   var productId = $(this).closest('product-data').find('.prod_id').val();
//   var token = $('input[name=csrfmiddlewaretoken]').val();
//   $.ajax({
//     type: "POST",
//     url: 'cart/add-to-cart',
//     data: {
//       productId: productId,
//       csrfmiddlewaretoken: token,
//     },
//     success: function (json) {
//       // console.log(json);
//     },
//     error: function (xhr, errmsg, err) {
//       // console.log(json);
//     },
//   });
// });

// var addToCart = document.getElementsByClassName("add-to-cart");

// Array.from(addToCart).forEach(function (btn) {
//   btn.addEventListener("click", function () {
//     var product_id = btn.dataset.product;
//     var action = btn.dataset.action;

//     console.log(product_id, action);
//     if (user === "AnonymousUser") {
//       // Apply a flas message here in future
//       console.log(
//         "You need to be a registered user before you can buy a product"
//       );
//     } else {
//       updateUserOrder(product_id, action);
//     }
//   });
// });

// function updateUserOrder(product_id, action) {
//   var url = "add/add_product/";
//   data = {
//     'product_id': product_id,
//     'action': action,
//   }

//   fetch(url, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify(data),
//   })
//     .then((response) => {
//       return response.json();
//     })
//     .then((data) => {
//       console.log("data:", data);
//     });
//   }
  
  // var cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
  // cartItems.push(data); // Assuming the response data represents a cart item
  // localStorage.setItem("cartItems", JSON.stringify(cartItems));







  document.addEventListener('DOMContentLoaded', function() {
    var addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');

            fetch('add/add-to-cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token if required
                },
                body: JSON.stringify({ product_id: productId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Item added to cart successfully, you can display a success message or update the UI accordingly
                    console.log('Item added to cart!');
                } else {
                    // Failed to add item to cart, handle the failure case
                    console.log('Failed to add item to cart!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});

// Helper function to retrieve CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function() {
  // Function to load the form into the modal
  function loadForm() {
    $.ajax({
      url: "{% url 'dashboard:create_product' %}",
      type: "GET",
      success: function(response) {
        $("#uploadProductModal .modal-content").html(response);
      },
      error: function(xhr, status, error) {
        console.error(xhr);
      }
    });
  }

  // Trigger the modal when the "Upload Product" link is clicked
  $("#uploadProductButton").click(function(e) {
    e.preventDefault();
    loadForm();
    $("#uploadProductModal").modal("show");
  });

  // Submit the form using AJAX when the "Create Product" button is clicked
  $(document).on("submit", "#uploadProductModal form", function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      type: form.attr("method"),
      data: form.serialize(),
      success: function(response) {
        $("#uploadProductModal").modal("hide");
        // Handle success response as needed
      },
      error: function(xhr, status, error) {
        console.error(xhr);
        // Handle error response as needed
      }
    });
  });
});

