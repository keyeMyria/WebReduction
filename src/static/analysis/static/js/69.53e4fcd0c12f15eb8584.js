webpackJsonp([69],{Jd7K:function(r,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=e("l2Cj"),n=e("t1Jn"),s=e("VU/8")(o.a,n.a,!1,null,null,null);t.default=s.exports},l2Cj:function(r,t,e){"use strict";var o=e("Dd8w"),n=e.n(o),s=e("NYxO");t.a={name:"VCorrSelect",created:function(){this.setDefaultVCorr()},data:function(){return{m1Error:!1,colltransError:!1,isDifferentVcorr:!1}},computed:n()({},e.i(s.a)("POWDER",{vcorrFiles:function(r){return r.normalizeFilesData.vcorr}}),e.i(s.a)("POWDER/Combine",{normalizeByVCorr:function(r){return r.normalizeByVCorr},selectedData:function(r){return r.selectedData}}),{items:function(){var r=[];for(var t in this.vcorrFiles)r.push({name:t,value:this.vcorrFiles[t]});return r},selected:{get:function(){return this.normalizeByVCorr},set:function(r){this.setNormalizeByVCorr(r)}},vcorrErrorMsg:function(){return this.m1Error&&this.colltransError?"Colltrans is not -80 nor 80 AND M1 is not 9.45 nor 0. Assuming VCorr Ge_115_OUT.":this.m1Error?"M1 is not 9.45 nor 0. Assuming VCorr Ge_115.":this.colltransError?"Colltrans is not -80 nor 80. Assuming VCorr OUT.":null},differentVcorrErrorMsg:function(){return this.isDifferentVcorr?"Atleast one or more files require different VCorr.":null}}),methods:n()({},e.i(s.d)("POWDER/Combine",["setNormalizeByVCorr"]),{resetVcorrErrors:function(){this.m1Error=!1,this.colltransError=!1,this.isDifferentVcorr=!1},vcorrErrors:function(){var r=this,t=[];return this.selectedData.forEach(function(e,o){e.vcorr.colltransError&&(r.isColltransError=!0),e.vcorr.m1Error&&(r.isM1Error=!0),!o||t.indexOf(e.vcorr.filename)>-1?t.push(e.vcorr.filename):r.isDifferentVcorr=!0}),!1},setDefaultVCorr:function(){var r=this.selectedData[0].vcorr.filename;this.selected=this.vcorrFiles[r],this.resetVcorrErrors(),this.vcorrErrors()}}),watch:{selectedData:function(){this.resetVcorrErrors(),this.vcorrErrors()}}}},t1Jn:function(r,t,e){"use strict";var o={render:function(){var r=this,t=r.$createElement,e=r._self._c||t;return e("div",[null!==r.vcorrErrorMsg?e("v-flex",{attrs:{xs12:""}},[e("v-alert",{staticClass:"pa-2",attrs:{outline:"",value:!0,type:"warning",transition:"fade-transition",icon:"fa-exclamation-triangle"}},[r._v(r._s(r.vcorrErrorMsg))])],1):r._e(),r._v(" "),null!==r.differentVcorrErrorMsg?e("v-flex",{attrs:{xs12:""}},[e("v-alert",{staticClass:"pa-2",attrs:{outline:"",value:!0,type:"warning",transition:"fade-transition",icon:"fa-exclamation-triangle"}},[r._v(r._s(r.differentVcorrErrorMsg))])],1):r._e(),r._v(" "),e("v-flex",{attrs:{xs12:""}},[e("v-select",{attrs:{items:r.items,"item-text":"name","item-value":"value",label:"VCorr (file to normalize data)",hint:"Select file to Normalize Data"},model:{value:r.selected,callback:function(t){r.selected=t},expression:"selected"}})],1)],1)},staticRenderFns:[]};t.a=o}});