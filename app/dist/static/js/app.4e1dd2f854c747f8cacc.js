webpackJsonp([1],{Gmvf:function(t,e){},NHnr:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("7+uW"),i=a("Gu7T"),r=a.n(i),s=a("Zrlr"),o=a.n(s),c=function t(e,a,n){o()(this,t),this.id=null,this.name="",this.description="",this.name=a,this.description=n,this.id=e},l=a("mtWM");var m=a("mtWM"),p=a.n(m),v={name:"App",data:function(){return{projects:[],diagrams:[],newName:"",newDescription:"",newDiagramType:"",currentProject:null,currentDiagram:null,showCreateNewProjectDialog:!1,showCreateNewDiagramDialog:!1,state:"project navigator"}},mounted:function(){this.projects=(l.get("/example2").then(function(t){return console.log(t)}),[new c(0,"Project 1","Project description"),new c(1,"Smandoprochi","Better then tamagochi"),new c(2,"Diagrams","Use-case diagrams"),new c(3,"Bricky","")])},methods:{addProject:function(){var t={id:this.projects.length,name:this.newName,description:this.newDescription};this.projects=[].concat(r()(this.projects),[t]),this.showCreateNewProjectDialog=!1,this.showProject(t)},openProject:function(t){var e=this;this.showProject(t),p.a.get("/getDiagrams").then(function(t){e.diagrams=t.data})},showProject:function(t){this.currentProject=t,this.state="diagram navigator",this.newName="",this.newDescription=""},addDiagram:function(){var t={id:this.projects.length,projID:this.currentProject.id,name:this.newName,description:this.newDescription,type:this.newDiagramType};this.diagrams=[].concat(r()(this.diagrams),[t]),this.showCreateNewDiagramDialog=!1,this.showDiagram(t)},showDiagram:function(t){this.currentDiagram=t,this.state="diagram editor",this.newName="",this.newDescription=""},goHome:function(){this.state="project navigator",this.currentDiagram=null,this.currentProject=null}},watch:{showCreateNewProjectDialog:function(){console.log(this.showCreateNewProjectDialog)}}},u={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"navbar"},[a("button",{staticClass:"btn btn-1",on:{click:function(e){return t.goHome()}}},[t._v("\n      Home\n    ")]),t._v(" "),"project navigator"===t.state?a("h1",[t._v("Project navigator")]):"diagram navigator"===t.state?a("h1",[t._v('Project "'+t._s(t.currentProject.name)+'"')]):"diagram editor"===t.state?a("h1",[t._v('Diagram "'+t._s(t.currentDiagram.name)+'"')]):t._e(),t._v(" "),"project navigator"===t.state?a("button",{staticClass:"btn btn-1 btn-sep icon-plus",on:{click:function(e){t.showCreateNewProjectDialog=!0}}},[t._v("\n      Create new project\n    ")]):t._e(),t._v(" "),"diagram navigator"===t.state?a("button",{staticClass:"btn btn-1 btn-sep icon-plus",on:{click:function(e){t.showCreateNewDiagramDialog=!0}}},[t._v("\n      Create new diagram\n    ")]):t._e()]),t._v(" "),"project navigator"===t.state?a("div",{staticClass:"projectTable"},t._l(t.projects,function(e){return a("div",{key:e.id,staticClass:"column"},[a("div",{staticClass:"card",on:{click:function(a){return t.openProject(e)}}},[a("p",[a("b",[t._v("Name:")]),t._v(" "+t._s(e.name))]),t._v(" "),a("p",[a("b",[t._v("Description:")]),t._v(" "+t._s(e.description))])])])}),0):"diagram navigator"===t.state?a("div",{staticClass:"projectTable"},t._l(t.diagrams,function(e){return a("div",{key:e.id,staticClass:"column"},[a("div",{staticClass:"card"},[a("p",[a("b",[t._v("Name:")]),t._v(" "+t._s(e.name))]),t._v(" "),a("p",[a("b",[t._v("Description:")]),t._v(" "+t._s(e.description))]),t._v(" "),a("p",[a("b",[t._v("Type:")]),t._v(" "+t._s(e.type))])])])}),0):t._e(),t._v(" "),t.showCreateNewProjectDialog?a("div",{staticClass:"newProjectModal",attrs:{id:"id01"}},[a("form",{staticClass:"newProjectModal-content"},[a("div",{staticClass:"formHeader"},[a("h1",[t._v("Create new project")]),t._v(" "),a("span",{staticClass:"closeForm",attrs:{title:"Close form"},on:{click:function(e){t.showCreateNewProjectDialog=!1}}},[t._v("X")])]),t._v(" "),a("hr"),t._v(" "),a("div",{staticClass:"newProjectForm"},[t._m(0),t._v(" "),a("input",{directives:[{name:"model",rawName:"v-model",value:t.newName,expression:"newName"}],attrs:{id:"NameProj",type:"text",placeholder:"Enter project name",name:"name",required:""},domProps:{value:t.newName},on:{input:function(e){e.target.composing||(t.newName=e.target.value)}}}),t._v(" "),t._m(1),t._v(" "),a("input",{directives:[{name:"model",rawName:"v-model",value:t.newDescription,expression:"newDescription"}],attrs:{id:"DescriptionProj",type:"text",placeholder:"Enter project description",name:"description"},domProps:{value:t.newDescription},on:{input:function(e){e.target.composing||(t.newDescription=e.target.value)}}}),t._v(" "),a("div",{staticClass:"newProjectButtons"},[a("button",{staticClass:"cancelbtn",attrs:{type:"button"},on:{click:function(e){t.showCreateNewProjectDialog=!1}}},[t._v("\n            Cancel\n          ")]),t._v(" "),a("button",{staticClass:"signupbtn",attrs:{type:"button"},on:{click:function(e){return t.addProject()}}},[t._v("Create")])])])])]):t._e(),t._v(" "),t.showCreateNewDiagramDialog?a("div",{staticClass:"newProjectModal"},[a("form",{staticClass:"newProjectModal-content"},[a("div",{staticClass:"formHeader"},[a("h1",[t._v("Create new diagram")]),t._v(" "),a("span",{staticClass:"closeForm",attrs:{title:"Close form"},on:{click:function(e){t.showCreateNewDiagramDialog=!1}}},[t._v("X")])]),t._v(" "),a("hr"),t._v(" "),a("div",{staticClass:"newProjectForm"},[t._m(2),t._v(" "),a("input",{directives:[{name:"model",rawName:"v-model",value:t.newName,expression:"newName"}],attrs:{id:"Name",type:"text",placeholder:"Enter diagram name",name:"name",required:""},domProps:{value:t.newName},on:{input:function(e){e.target.composing||(t.newName=e.target.value)}}}),t._v(" "),t._m(3),t._v(" "),a("input",{directives:[{name:"model",rawName:"v-model",value:t.newDescription,expression:"newDescription"}],attrs:{id:"Description",type:"text",placeholder:"Enter diagram description",name:"description"},domProps:{value:t.newDescription},on:{input:function(e){e.target.composing||(t.newDescription=e.target.value)}}}),t._v(" "),t._m(4),t._v(" "),t._m(5),t._v(" "),a("div",{staticClass:"newProjectButtons"},[a("button",{staticClass:"cancelbtn",attrs:{type:"button"},on:{click:function(e){t.showCreateNewDiagramDialog=!1}}},[t._v("\n            Cancel\n          ")]),t._v(" "),a("button",{staticClass:"signupbtn",attrs:{type:"button"},on:{click:function(e){return t.addDiagram()}}},[t._v("Create")])])])])]):t._e()])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"NameProj"}},[e("b",[this._v("Name")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"DescriptionProj"}},[e("b",[this._v("Description")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"Name"}},[e("b",[this._v("Name")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"Description"}},[e("b",[this._v("Description")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",[e("b",[this._v("Diagram Type")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("select",[e("option",[this._v("strict")]),this._v(" "),e("option",[this._v("free")])])}]};var d=a("VU/8")(v,u,!1,function(t){a("Gmvf")},null,null).exports,h=a("/ocq");n.a.use(h.a);var _=new h.a({routes:[]});n.a.config.productionTip=!1,new n.a({el:"#app",router:_,components:{App:d},template:"<App/>"})}},["NHnr"]);
//# sourceMappingURL=app.4e1dd2f854c747f8cacc.js.map