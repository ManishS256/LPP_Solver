const homepage = {
  methods:{
    
  },
  template:`<div>
	<h3 style="color:rgb(142, 68, 173)"><br>
		Instructions on how to submit the Question
	</h3>
	<h5>
		<ol style="color:rgb(243, 156, 18)" >
			<li>The question to be solved can be typed in the app itself or can be typed in a text file and can be uploaded</li>
			<li>The first line should mention the problem's type<ul><li>max - Maximization Type</li><li>min - Minimization Type</li></ul>
			<li>The second line should have the cost co-efficients of objective function</li>
			<li>The third line should have the words "subject to" to depict that the following are constraints</li>
			<li>The fourth line should have co-efficients of the costraint number 1</li>
			<li>The fifth line should mention the constraint type<ul><li>gt - Greater than</li><li>lt - Less than</li><li>eq - Equal to</li></ul></li>
			<li>The seventh line should have the RHS of constraint one</li>
			<li>Follow steps 5 and 6 for the remaining constraints </li>
			<li>After entering all these things the last line should have end to depict that all constraints have been entered</li>
		</ol>
	</h5>
</div>`,
}
const typeqn = {
  data: function(){
  	return{
  		qn:"",
  		st:false,
  		soln:"",
  	}
  },
  methods:{
  	solve: async function(){
  		url="/api/solve/type";
      	a=await fetch(url,{method: 'PUT', body: this.qn});
        response=await a.json();
        console.log(response)
      	response = response.replace(/(\n)/g, '<br>');
        this.soln=response
        this.st=true
  	}
  },
  template:`<div><div class="mb-3" style="text-align:center"><br>
				<label for="exampleFormControlTextarea1" class="form-label" ><h5>Enter Your Question Here</h5></label>
			  	<textarea class="form-control" id="exampleFormControlTextarea1" rows="13" style="background-color:powderblue" v-model="qn">
			  	</textarea><br>
			  	<button class="btn btn-primary" v-on:click="solve">Solve</button>
          <div v-if="st" style="text-align:left">
          <h4 style="color:rgb(241, 196, 15)">Solution:</h4><h6 v-html="soln"></h6>
          </div>
		  	</div></div>`,
}
const fileqn = {
  data: function(){
  	return{
  		st:false,
  		soln:"",
  	}
  },
  methods:{
    solve: async function(){
      var input = document.getElementById('fileupload');
      const data = new FormData();
      data.append('impfile', input.files[0]);
      a= await fetch('/api/solve/file', {
        method: 'PUT',
        body: data
      })
      response=await a.json();
      console.log(response)
      response = response.replace(/(\r\n|\r|\n)/g, '<br>');
      this.soln=response
      this.st=true
    }
  },
  template:`<div  style="text-align:center"><br>
  	<div style="text-align:left">
  		<h4 style="color:rgb(142, 68, 173)">
		Instructions on how to submit the File
		</h4>
		<ol style="color:rgb(243, 156, 18)"><h5>
			<li>The File needs to be a Text file (.txt file)</li>
			<li>The content needs to be typed in the file is same as what needs to be typed in the text box</li>
			<li>These instructions are provided in Instructions tab. Refer that if clarification is needed</li></h5><br>
		</ol>
  	</div>
    <div class="input-group">
    <input type="file" accept=".txt" class="form-control" id="fileupload" name="filecsv" aria-describedby="inputGroupFileAddon04" aria-label="Upload" required>
    </div>
    <br><button class="btn btn-primary" v-on:click="solve">Submit</button><br><br>
    <div v-if="st" style="text-align:left">
    <h4 style="color:rgb(241, 196, 15)">Solution:</h4><h6 v-html="soln"></h6>
    </div>
    </div>`,
}



const routes = [
{ path: '/', name: 'Instructions', component: homepage },
{ path: '/solve/type', name: 'Type Question', component: typeqn },
{ path: '/solve/file', name: 'Upload Question', component: fileqn },
]


const router = new VueRouter({
routes,
base: '/',
})

let app = new Vue({
    el: '#app',
    data: {
      
    },
    router,
    methods: {
      
    },
  })