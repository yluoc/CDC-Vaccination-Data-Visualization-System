function ajaxGetRequest(path, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
        callback(this.response);
    }
  };
  request.open("GET", path);
  request.send();
}

function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
      callback(this.response);
    }
  };
  request.open("POST", path);
  request.send(data);
}

function barData(){
  ajaxGetRequest("/showBar",showBar);
} 

function showBar(response){
  let list_x = [];
  let list_y = [];
  let dic = JSON.parse(response);

  for (let key of Object.keys(dic)){
    list_x.push(key);
  }

  for (let value of Object.values(dic)){
    list_y.push(value);
  }
  
  var data = [
  {
    x: list_x,
    y: list_y,
    type: 'bar'
  }
  ];
  data = Plotly.newPlot('myDiv', data); 
  
}



function pieData(){
  ajaxGetRequest("/showPie",showPie);
}

function showPie(response){

  let dic = JSON.parse(response);
  let list_label = [];
  let list_value = [];

  for (let label of Object.keys(dic)){
    list_label.push(label);
  }
  for (let value of Object.values(dic)){
    list_value.push(value);
  }

  var data = [{
  values: list_value,
  labels: list_label,
  type: 'pie'
  }];

  var layout = {
  height: 400,
  width: 500
  };

  Plotly.newPlot('myDiv2', data, layout);
}


function textmassage(){
  let content = document.getElementById("locText");
  content = content["value"];
  console.log(content);

  ajaxPostRequest("/showLine",content,showLine);
}

function showLine(response){
  let list_x = [];
  let list_y = [];
  let list = JSON.parse(response);
  for (let dic of list){
    list_x.push(dic["date"]);
    list_y.push(dic["series_complete_pop_pct"]);

  var trace1 = {
  x: list_x,
  y: list_y,
  type: 'scatter'
  };

  var data = [trace1];

  Plotly.newPlot('myDiv3', data);
  }
}


