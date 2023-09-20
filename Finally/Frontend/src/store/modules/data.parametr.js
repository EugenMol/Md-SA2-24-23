import data from '@/api/data';

export default {
    state: {
        query: {},
        query_min30: {}
    },

    getters: {
        QUERY(state) {
            return state.query;
        },
        QUERY_MIN30(state) {
            return state.query_min30;
        },
    },
    mutations: {
        SET_QUERY: (state, query) => {
            state.query = query;
        },
        SET_QUERY_MIN30: (state, query) => {
            state.query_min30 = query;
        },
    },
    actions: {
        GET_DATA_FROM_QUERY({commit}, query) {
            data.get_data(query.cmd, query.vm_id, query.from, query.to)
                .then((response) => {
                    commit('SET_QUERY', response.data);
                    return response;
                });
        },
        GET_MIN_30_FROM_QUERY({commit}, query) {
            data.getmin_30(query.vm_id, query.from, query.to, 'ep')
                .then((response) => {
                    commit('SET_QUERY_MIN30', response.data);
                    return response;
                });
        },


        GET_CREATE_CMD({commit}, query) {
            data.create_cmd(query)
                .then((response) => {
                    commit('SET_QUERY', response.data);
                    return response;
                });
        }
    }
}