(window.webpackJsonp=window.webpackJsonp||[]).push([["2mTh"],{R0mg:function(i,a,r){"use strict";var t=r("TqRt");Object.defineProperty(a,"__esModule",{value:!0}),a.UPDATE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=a.GET_OFFICIAL_CLARIFICATIONS_WITH_REPORTER_QUERY=a.GET_OFFICIAL_CLARIFICATIONS_WITHOUT_REPORTER_QUERY=a.DELETE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=a.CREATE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=void 0,a.createOfficialClarification=function(i,a,r,t,e,c){return i.mutate(E,{variables:{clarification:{youtubeId:a,reporterKaid:r,openTimestamp:e,closeTimestamp:c,text:t}},refetchQueries:["getOfficialClarificationsWithReporter"]}).then((i=>{var a;if(null!=(a=i.data)&&a.createOfficialClarification.error)throw new o.KAError(i.data.createOfficialClarification.error.code,o.Errors.GraphqlResponse);return i.data.createOfficialClarification.newClarification})).catch((i=>{throw new o.KAError("Failed to create new clarification",o.Errors.Internal,{cause:i})}))},a.deleteOfficialClarification=function(i,a){return i.mutate(h,{variables:{id:a},refetchQueries:["getOfficialClarificationsWithReporter"]}).then((i=>{var a;if(null!=(a=i.data)&&a.deleteOfficialClarification.error)throw new o.KAError(i.data.deleteOfficialClarification.error.code,o.Errors.GraphqlResponse);return!0})).catch((i=>{throw new o.KAError("Failed to delete clarification",o.Errors.Internal,{cause:i})}))},a.getOfficialClarifications=function(i,a){return i.query(_,{variables:{youtubeId:a},fetchPolicy:"network-only"}).then((i=>i.data.officialClarifications)).catch((i=>{throw new o.KAError("Failed to fetch clarifications",o.Errors.Internal,{cause:i})}))},a.updateOfficialClarification=function(i,a,r,t,e,c){return i.mutate(A,{variables:{id:a,clarification:{youtubeId:r,openTimestamp:e,closeTimestamp:c,text:t}},refetchQueries:["getOfficialClarificationsWithReporter"]}).then((i=>{var a;if(null!=(a=i.data)&&a.updateOfficialClarification.error)throw new o.KAError(i.data.updateOfficialClarification.error.code,o.Errors.GraphqlResponse);return i.data.updateOfficialClarification.updatedClarification})).catch((i=>{throw new o.KAError("Failed to update clarification",o.Errors.Internal,{cause:i})}))};var e=t(r("lTCR")),c=r("8r+/"),o=r("4PhQ");let f,n,l,I,u,d,O,C=i=>i;const T=(0,e.default)(f||(f=C`
    fragment clarificationFragment on OfficialClarification {
        id
        text
        openTimestamp
        closeTimestamp
        youtubeId
    }
`)),s=(0,e.default)(n||(n=C`
    ${0}

    fragment clarificationFragmentWithReporter on OfficialClarification {
        reporter {
            id
            kaid
            nickname
            avatarSrc: avatarUrl
        }
        ...clarificationFragment
    }
`),T),_=(0,c.gqlOp)((0,e.default)(l||(l=C`
    query getOfficialClarificationsWithReporter($youtubeId: String!) {
        officialClarifications(youtubeId: $youtubeId) {
            ...clarificationFragmentWithReporter
        }
    }

    ${0}
`),s));a.GET_OFFICIAL_CLARIFICATIONS_WITH_REPORTER_QUERY=_;const p=(0,c.gqlOp)((0,e.default)(I||(I=C`
    query getOfficialClarifications($youtubeId: String!) {
        officialClarifications(youtubeId: $youtubeId) {
            ...clarificationFragment
        }
    }

    ${0}
`),T));a.GET_OFFICIAL_CLARIFICATIONS_WITHOUT_REPORTER_QUERY=p;const E=(0,c.gqlOp)((0,e.default)(u||(u=C`
    mutation createOfficialClarification(
        $clarification: CreateOfficialClarificationInput!
    ) {
        createOfficialClarification(clarification: $clarification) {
            newClarification {
                ...clarificationFragmentWithReporter
            }
            error {
                code
            }
        }
    }

    ${0}
`),s)),R=E;a.CREATE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=R;const A=(0,c.gqlOp)((0,e.default)(d||(d=C`
    mutation updateOfficialClarification(
        $id: ID!
        $clarification: UpdateOfficialClarificationInput!
    ) {
        updateOfficialClarification(id: $id, clarification: $clarification) {
            updatedClarification {
                ...clarificationFragmentWithReporter
            }
            error {
                code
            }
        }
    }

    ${0}
`),s)),F=A;a.UPDATE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=F;const h=(0,c.gqlOp)((0,e.default)(O||(O=C`
    mutation deleteOfficialClarification($id: ID!) {
        deleteOfficialClarification(id: $id) {
            error {
                code
            }
        }
    }
`))),m=h;a.DELETE_OFFICIAL_CLARIFICATION_MUTATION_FOR_TEST=m}}]);
//# sourceMappingURL=../../sourcemaps/en/2mTh.d47f36795834f761fc09.js.map