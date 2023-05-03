// Add item to list
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});

// Remove last item from list
$('DIV#remove_item').click(function () {
  $('UL.my_list li:last-child').remove();
});

// Clear entire list
$('DIV#clear_list').click(function () {
  $('UL.my_list').empty();
});
