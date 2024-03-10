#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "list_utils.h"

bool list_insert_all(list *dest, size_t index, const list *src){
    if ((index > list_size(dest)) || (src == NULL) || (dest == NULL) || (src == dest)){
        return false;
    }
    else if (index == list_size(dest)){
       for(size_t i = 0;i < list_size(src); i++){
            list_add(dest,list_get(src,i));
        }
        return true; 
    } 
    else
    {   
        memcpy(dest+list_size(src),)
        memcpy(dest+index,src,list_size(src));
    }
}

list *list_split_at(list *t, size_t index){

}

