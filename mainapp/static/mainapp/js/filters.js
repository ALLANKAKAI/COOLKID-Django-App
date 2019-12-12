
$('#gender').change(function(){
const gender = $(this).val();

const county = $('#county').val();

 location.href = `/dashboard?gender=${gender}&county=${county}`;


})


$('#county').change(function(){
const gender = $('#gender').val();

const county = $(this).val();

 location.href = `/dashboard?gender=${gender}&county=${county}`;

})