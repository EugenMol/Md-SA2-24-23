import data from '@/api/data';

export default {
    state: {
        dataset_1: {},
    },

    getters: {
        DATASET_1(state) {
            return state.dataset_1;
        },
    },
    mutations: {
        SET_DATASET_1: (state, payload) => {
            state.dataset_1 = payload;
        },
    },
    actions: {
        GET_DATASET_1_FROM_API({commit}, payload) {
            data.get_data_to_dash_1(payload.vm_id, payload.energy, payload.date)
                .then((response) => {
                    commit('SET_DATASET_1', response.data);
                    return response;
                });
        },

    }
}
