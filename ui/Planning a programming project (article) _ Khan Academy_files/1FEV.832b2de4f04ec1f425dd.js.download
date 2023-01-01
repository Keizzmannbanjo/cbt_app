(window.webpackJsonp=window.webpackJsonp||[]).push([["1FEV"],{VHtk:function(e,t,r){"use strict";var s=r("TqRt");Object.defineProperty(t,"__esModule",{value:!0}),t.isDismissed=t.dismiss=t.QUERY=t.DISMISS_UNTIL_MUTATION=void 0;var i=s(r("lTCR")),a=function(e,t){if(!t&&e&&e.__esModule)return e;if(null===e||"object"!=typeof e&&"function"!=typeof e)return{default:e};var r=u(t);if(r&&r.has(e))return r.get(e);var s={},i=Object.defineProperty&&Object.getOwnPropertyDescriptor;for(var a in e)if("default"!==a&&Object.prototype.hasOwnProperty.call(e,a)){var n=i?Object.getOwnPropertyDescriptor(e,a):null;n&&(n.get||n.set)?Object.defineProperty(s,a,n):s[a]=e[a]}s.default=e,r&&r.set(e,s);return s}(r("4PhQ")),n=r("8r+/");let o,d,m=e=>e;function u(e){if("function"!=typeof WeakMap)return null;var t=new WeakMap,r=new WeakMap;return(u=function(e){return e?r:t})(e)}const l=(0,n.gqlOp)((0,i.default)(o||(o=m`
    query UserHasDismissedQuery($itemName: String!) {
        dismissedItem(itemName: $itemName) {
            id
            isDismissed
        }
    }
`)));t.QUERY=l;const c=(0,n.gqlOp)((0,i.default)(d||(d=m`
    mutation DismissItemMutation($itemName: String!, $expires: DateTime) {
        dismissItem(itemName: $itemName, expires: $expires) {
            error {
                code
            }
            dismissedItem {
                id
                isDismissed
            }
        }
    }
`)));t.DISMISS_UNTIL_MUTATION=c;t.isDismissed=(e,t)=>e.query(l,{variables:{itemName:t},fetchPolicy:"cache-first"}).then((e=>{var t,r;return Boolean(null==(t=e.data)||null==(r=t.dismissedItem)?void 0:r.isDismissed)})).catch((e=>(a.default.log(`Failed to query dismiss state for dismissKey: ${t}`),!0)));t.dismiss=(e,t,r)=>((e,t,r)=>{const s=r.toISOString();e.mutate(c,{variables:{itemName:t,expires:s}}).then((e=>{var t,r;if(null!=(null==(t=e.data)||null==(r=t.dismissItem)?void 0:r.error)){const{code:t}=e.data.dismissItem.error,r=new a.KAError(t,a.Errors.GraphqlResponse);throw r.errorCode=t,r}return e})).catch((e=>{a.default.error("Failed to mutate dismiss state",a.Errors.TransientKhanService,{cause:e,sentryData:{contexts:{extras:{dismissKey:t,expiresString:s,errorCode:e.errorCode}}}})}))})(e,t,(e=>{const t=new Date(3e3,6,1);if("never"===e)return t;const r=(new Date).getTime();return new Date(r+864e5*e)})(r))}}]);
//# sourceMappingURL=../../sourcemaps/en/1FEV.832b2de4f04ec1f425dd.js.map