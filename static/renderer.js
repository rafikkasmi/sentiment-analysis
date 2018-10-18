
var myBtn = document.getElementById('bu');

  //add event listener
  myBtn.addEventListener('click', function(event) {
  	


var text=document.getElementById('Sn').value
document.getElementById('mt').innerHTML="Hold On ....";

// var options={
// mode: 'text',
//   pythonPath: '/usr/bin/python3',
//   pythonOptions: ['-u'], // get print results in real-time
//   scriptPath: '',
//   args: [text]
// }
// console.log("finish")
// pythonProcess.stdout.on('data', (data) => {
var data,obj,happiness,sadness;
    $.ajax({url: "http://127.0.0.1:5000/api/'"+text+"'", success: function(result){
        data=result
        obj=JSON.parse(data)
        happiness=obj.happiness*100
        sadness=obj.sadness*100
        console.log(happiness,sadness)

	document.getElementById('mt').innerHTML="Sentiment Analysis";

	hhp=(happiness)*300/100
	hhp=hhp+"px"
	$(".happiness").show();
	$(".happiness").animate({height: hhp});
	  $('.happiness p').each(function () {
  var $this = $(this);
  jQuery({ Counter: 0 }).animate({ Counter: happiness }, {
    duration: 1000,
    easing: 'swing',
    step: function () {
      $this.text(Math.round(this.Counter)+"%");
    }
  });
});
	hsd=(sadness)*300/100
	hsd=hsd+"px"
	$(".sadness").show();
	$(".sadness").animate({height: hsd});
	  $('.sadness p').each(function () {
  var $this = $(this);
  jQuery({ Counter: 0 }).animate({ Counter: sadness }, {
    duration: 1000,
    easing: 'swing',
    step: function () {
      $this.text(Math.round(this.Counter)+"%");
    }
  });
});
    console.log(hhp)
// });
    },
    error: function(result){
        document.getElementById('mt').innerHTML="Sentiment Analysis";
      alert("Wait For The Model to train")

    }

  });

});