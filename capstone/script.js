function showSection(id){

    let sections =
    document.querySelectorAll('.section');

    sections.forEach(sec=>{
        sec.style.display='none';
    });

    document.getElementById(id).style.display='block';
}

function drawBox(){

    let canvas =
    document.getElementById("screen");

    let ctx =
    canvas.getContext("2d");

    ctx.fillStyle="black";

    // row 79 simulation
    ctx.fillRect(
        0,
        79,
        64,
        20
    );
}

function clearBox(){

    let canvas =
    document.getElementById("screen");

    let ctx =
    canvas.getContext("2d");

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );
}